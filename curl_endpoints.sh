#!/usr/bin/env bash
# Run curl tests for all API endpoints.
set -euo pipefail

BASE_URL='http://127.0.0.1:8000'
CURL_COMMON_OPTS=(--silent --show-error --fail --header "Accept: application/json")

# Perform a GET request and print body and HTTP code.
get_json() {
  local path="$1"
  local url="${BASE_URL}${path}"
  local body_file http_code

  body_file="$(mktemp)"
  http_code=$(curl "${CURL_COMMON_OPTS[@]}" --output "$body_file" --write-out "%{http_code}" --request GET "$url" || true)

  echo "GET ${path}"
  cat "$body_file"
  echo
  echo "HTTP ${http_code}"
  rm -f "$body_file"
  echo
}

# Perform a POST with JSON body and print body and HTTP code.
post_json() {
  local path="$1"
  local json_body="$2"
  local url="${BASE_URL}${path}"
  local body_file http_code

  body_file="$(mktemp)"
  http_code=$(curl "${CURL_COMMON_OPTS[@]}" --header "Content-Type: application/json" --data "$json_body" --output "$body_file" --write-out "%{http_code}" --request POST "$url" || true)

  echo "POST ${path}"
  echo "Request: ${json_body}"
  cat "$body_file"
  echo
  echo "HTTP ${http_code}"
  rm -f "$body_file"
  echo
}

# Test /health endpoint.
get_health() { get_json "/health"; }

# Test /time endpoint.
get_time() { get_json "/time"; }

# Test /greet endpoint with a valid payload.
post_greet() {
  local name="${1}"
  post_json "/greet" "{\"name\":\"${name}\"}"
}

# Test /greet endpoint with an invalid payload to trigger validation error.
post_greet_invalid() { post_json "/greet" "{}"; }

main() {
  echo "Base URL: ${BASE_URL}"
  echo
  get_health
  get_time
  post_greet "Joe"
  post_greet_invalid
}

main "$@"
