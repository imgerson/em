#Em

Little Python class that allows me to connect to Gmail and send emails for me. It's pretty basic.

Will be working on it based on my own needs. Please feel free to fork/contribute in any way you want.

Here's an example of what it does. 


```python
#!/usr/bin/env python3


from em import ConfigEm, Em


subject = 'Hey There'
message = 'Hello World.'

conf = ConfigEm()
conf.user = 'email@gmail.com'
conf.user_password = '!passwordomg!'

em = Em(conf=conf)
em.login()
em.set_message(toaddr='someemail@gmail.com', subject=subject,
    message=message)
em.attach(attachment='pdf.pdf')
em.send()
em.logout()
```
