invalid_credentials = (401, "Invalid credentials")
invalid_name = (401, "Name already exists")
match_not_found = (404, "Match not found")
wrong_inputs = (401, "Wrong inputs")
unauthorized_access_to_admin_api = (401, "Unauthorized access to admin API")
invalid_token = (401, "Invalid token. Registeration and / or authentication required")
expired_token = (401, "Expired token. Reauthentication required.")
invalid_team_id = (
    400,
    "Invalid team id. Retry with a uuid or ISO 3166-1 alpha-2 code.",
)
team_not_found = (404, "No team found for the requested id.")
