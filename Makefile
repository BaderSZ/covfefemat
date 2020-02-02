SERVER=brewd
CLIENT=coffee
INSTALL_DIR=/usr/local/etc/covfefemat/

.PHONY=all default doc

all: default

default:

run:
	FLASK_APP=server/brewd.py FLASK_DEBUG=1 flask run

clean: clean-code clean-doc

clean-code:
	rm -rf __pycache__/
	
install: install-client install-server

install-client:
	sudo cp ${PWD}/client/${CLIENT}.py /usr/local/bin/${CLIENT}

install-server:
	sudo mkdir -p ${INSTALL_DIR}
	sudo cp ${PWD}/server/* ${INSTALL_DIR}
	sudo ln -s ${INSTALL_DIR}/brewd.py /usr/local/bin/${SERVER}

#Doc section
doc:
	pdflatex -halt-on-error -output-directory docs/ -output-format pdf docs/XHTCPCP.tex

clean-doc:
	rm -f docs/{XHTCPCP.pdf,XHTCPCP.toc,XHTCPCP.aux,XHTCPCP.out,XHTCPCP.log}
