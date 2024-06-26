'''
Leetcode 929. Unique Email Address
[Easy][Topics][Companies]

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
'''
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        #count = 0
        #duplicate_list = {}
        #for email in emails:
        #    duplicate = set(email)
        #    if duplicate in duplicate_list:
        #        count+=1
        #    else:
        #        duplicate_list.add(duplicate)
        #return count
        unique_emails = set()

        for email in emails:
            local_name, domain_name = email.split('@')
            
            # Remove all characters following the first '+' in the local name
            local_name = local_name.split('+')[0]
            
            # Remove all dots '.' from the local name
            local_name = local_name.replace('.', '')
            
            # Reconstruct the email address and add it to the set of unique emails
            normalized_email = local_name + '@' + domain_name
            unique_emails.add(normalized_email)
        
        return len(unique_emails)
    
my_instance = Solution()
emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]
print('test1 = ', my_instance.numUniqueEmails(emails))

emails = ["a@leetcode.com",
          "b@leetcode.com",
          "c@leetcode.com"]
print('test2 = ', my_instance.numUniqueEmails(emails))