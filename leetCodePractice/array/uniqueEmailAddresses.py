class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def formatEmail(email):
            ampersand = email.index("@")
            localName = email[0:ampersand]
            domain = email[ampersand:]
            newLocal = ""
            for letter in localName:
                if letter == ".":
                    next
                elif letter == "+":
                    break
                else:
                    newLocal += letter
                    
            return newLocal+domain
        
        if len(emails) == 0:
            return 0
        
        record = []
        
        for email in emails:
            formatted = formatEmail(email)
            if formatted not in record:
                record.append(formatted)
                
        return len(record)