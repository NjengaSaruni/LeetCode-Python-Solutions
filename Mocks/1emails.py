def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0]
        local = ''.join(local.split('.'))
        unique_emails.add(f'{local}@{domain}')

    return len(unique_emails)

if __name__ == '__main__':
    print(numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    ))