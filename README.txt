

coffee.*: python3 and bash cli client for htcpcp, xhtcpcp compatible

pi: harware and gpio programming/management
pot: The control class: manages the flask/brewd responses and runs appropriate actions 
brewd: The brew daemon, flask-based (x)htcpcp server, htcpcp compatible


 * flask (install via pip as flask, or debian package python3-flask)
 * ntpd, because memetics of flask clocks
 * RPi.GPIO (install via pip) https://pypi.org/project/RPi.GPIO/
 * logging (python3 default, iirc)
 * pdflatex for documentation
usage:
call method is coffee://<host>/pot with METHODs documented
							  /about returns status and coffee info
							  /teapot returns memetics response
							  
TODO:
possible additions:
log: daemon or library to clean up logging works?


TODO: bash and python clients and debug server/daemon
     - htcpcp(s)?

