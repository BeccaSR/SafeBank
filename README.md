# SafeBank

A python banking app programme.

This programme was made during the HyperionDev Data Science Bootcamp. The project was designed to practice and highlight the python skills learnt so far, including:

- principles and importance of defensive programming in real-world applications
- recognising and addressing various eror types: user-induced, environmental and logial
- implementing conditional statements for effective input validation
- exception handling in Python
- designing custom exceptions for specific error scenarios
  
Case Study Story:

In the digital age, online banking has become the norm. 
SafeBank, a leading financial institution, is looking to revamp its online banking interface to ensure it's not only user-friendly but alos robust against potential errors and misuse.

The new system should allow users to perfrom common banking operations like checking balances, transferring funds and depositing or withdrawing money.
However, with the convenience of online banking comes the responsibility of ensuring transactions are error-free and secure.
For instance, a user shouldn't be able to transfer negative amounts or over-withdraw beyond their account balance.

Students are tasked with designing this new interface.
They must implement defensive measures to handle common issues.
If a user tries to withdraw more than their current balance, the system should raise an 'InsufficientFundsError'.
These custom exceptions, along with other others, will ensure that errors are not only prevented but also communicated clearly to the user.
