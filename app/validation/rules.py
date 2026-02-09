def validate_response(corep_json):

    errors = []

    for field in corep_json.get("fields", []):

        if field["field_code"].lower() == "cet1":

            try:
                value = float(field["value"])

                if value < 0:
                    errors.append("CET1 cannot be negative.")

            except:
                errors.append("Invalid numeric value for CET1.")

    return errors
