# aws-challenge
Question from Amazon interview

You have access log from a host serving Amazon.com traffic, with information about request timestamps, UserIdentifiers, the product page url and Status Code of the request.

$ tail -f access.log

02 Mar 2016 21:55:05,379    User:user1  URL:canonT2i.html StatusCode:200
02 Mar 2016 21:55:06,379    User:user2  URL:nikonD5000.html StatusCode:200
02 Mar 2016 21:55:07,379    User:user1  URL:tripod.html StatusCode:200
02 Mar 2016 21:55:07,380    User:user3  URL:canonT2i.html StatusCode:200
02 Mar 2016 21:55:07,381    User:user2  URL:tripod.html StatusCode:200
02 Mar 2016 21:55:08,381    User:user3  URL:tripod.html StatusCode:200

Given such an access log, you have to find the most popular page sequence consisting of 2 pages across all users.

In this sample log, you see that the most popular page sequence is

canonT2i.html -> tripod.html

This was the page sequence that was visited by user1 and user3.
