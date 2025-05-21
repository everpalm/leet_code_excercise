'''
Reference a dictionary and expand variable in a multi-lines text content with
support following prefixes (inorder) for any variable “{var}”
ul_: replace space(s) with '_'
ns_: replace space with ' '
ca_: capitalize each words
lc_: lower case
uc_: upper case

Input:
	Content: “hello {lc_title} {name},\nIt is your email {ul_lc_name}@ust.com
    and formal signature {ca_name} and profile name is {ns_lc_name}.”.
	Vardict: {“name”: “foo Bar”, “title”: “Miss”}
Output: 
	hello miss foo Bar,\nIt is your email foo_bar@ust.com and formal signature
    Foo Bar and profile name is foobar.
PS: “import re” if need
'''
