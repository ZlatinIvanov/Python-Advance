from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_LENGTH = 4
DOMAIN_NAME = (".bg", ".com", ".org", ".net")

pattern_name = r'\w+'
domain_name = r'[\.][A-z]+'

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Your email should contain only one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if findall(pattern_name, email)[0] != email.split("@")[0]:
        raise InvalidNameError("Name should contain only letters, digits and underscores!")
    if findall(domain_name, email)[0] not in DOMAIN_NAME:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
