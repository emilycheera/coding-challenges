def num_unique_emails(emails):

    res_emails = set()
    
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        res_emails.add(local + "@" + domain)
        
    return len(res_emails)