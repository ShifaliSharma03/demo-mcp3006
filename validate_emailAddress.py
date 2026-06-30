"""Utility to validate email addresses."""

import re


# Basic RFC-style pattern for common email formats.
EMAIL_PATTERN = re.compile(
	r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
	r"@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9]"
	r"(?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def is_valid_email(email: str) -> bool:
	"""Return True if the email address format is valid, else False."""
	if not isinstance(email, str):
		return False

	candidate = email.strip()
	if not candidate or " " in candidate:
		return False

	if len(candidate) > 254:
		return False

	local_part, sep, domain = candidate.rpartition("@")
	if sep == "" or not local_part or not domain:
		return False
if len(local_part) > 64:
prin
		return False

	return EMAIL_PATTERN.fullmatch(candidate) is not None


if __name__ == "__main__":
	user_input = input("Enter an email address: ").strip()
	if is_valid_email(user_input):
		print("Valid email address")
	else:
		print("Invalid email address")

