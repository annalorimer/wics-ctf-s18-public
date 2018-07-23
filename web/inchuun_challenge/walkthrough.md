This is a path traversal challenge! With a twist.

1. Visit the server's index page at [IP]:[PORTNUMBER,default 8080].
2. Click on "YOU MAY BEGIN" to enter the exam.
3. See that the exam questions are very hard.
4. Notice that the path at the top of the first page of 
questions is number one. By changing it to '2' instead of '1',
see that a new page of the exam is loaded.
5. Notice that at page 5, the message is slightly different.
Numbers past 5 and invalid values (strings) take you back to the
exam entrance page.
6. Examing the HTML of the valid exam pages and notice that page 5's
message mentions that specifically the answers are not available during the exam.
7. Use the path to the images of the exam content from the valid pages
(1 to 4) to construct the path to the exam image for page 5.
8. Load the exam image for page 5 (the answer key!) at /exam_data/pg_05.png
9. Remove the background colour to show the image
10. See that the value of tau is 0.055 and that the flag is the part after
the decimal point. The flag is 055.
