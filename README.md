![Interclaustra logo](https://github.com/Approximately-82-kangaroos/interclaustra/blob/main/logo.png)

This repo is NOT complete

This is a remake of a project I made in high school which was lost to a hard drive failure, meant to allow for distributed computing to be accessible to all who can write Python code.

## TODO list:
- Create socket servers (Done)
- Create file transfer (Done, janky. Sends entire file at once, not 1024-size packets)
- Create function argument transfer (Done)
- Create function processing on client (Done)
  - Add multithreading support
- Create function result transfer (Done)
- Create secondary verification on server

# How does/should it work at a high level?

Step 1: Bob starts up the server

Step 2: Alice connects with her client

Step 3: Bob sends his problem's solution script to Alice

Step 4: Bob sends his problem's parameters to Alice

Step 5: Alice computes the problem and sends the solution back to Bob

Step 6: Bob verifies the solution and does with it as he wishes

Step 7: Bob loads new parameters, rinse and repeat from Step 4 until someone closes the connection
