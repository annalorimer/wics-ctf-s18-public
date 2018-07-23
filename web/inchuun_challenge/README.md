# inchuun challenge

To run this challenge:
- enter the `./code` directory
- set up a python virtualenv in `./code` using python2 (`virtualenv . -p python2`)
  - (If you don't have `virtualenv` installed - `sudo pip install virtualenv`)
- activate the virtualenv with `source ./bin/activate`
- `pip install -r requirements.txt`
- `python inchuun_server.py --port {any port number}` or `python -m inchuun_server -p {port number}`
  - you can supply the `-h` or `--help` options to `python inchuun_server.py` to
	see what it supports (should be just the port number option)
- the server will also output its port number on startup.
- when you're done, kill the server with ctrl-C and run `deactivate` to exit the virtualenv
