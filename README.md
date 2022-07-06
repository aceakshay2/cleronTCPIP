# cleronTCPIP
Here  ,  establish communication between 2 devices using TCP/IP protocol

For the past few days , I had been struggling with 1 problem. 
That is  , When I ran my code on jupyter notebook , The server side of code seemed to send/receive data. When I ran the same code on windows powershell , it always output none. As it turns out , It was because the receive_data() function did not have a return value.  I have updated the code with the receive_data function return the value  when it is called.

