QR_URL := https://smll.info/

DPI := 72
ERR_CORR := L
MARGINS := 1
SIZE := 1
#MICRO := -M

help:
	@echo try "qr"

smll-qr.%:
	qrencode -d $(DPI) -s $(SIZE) -l $(ERR_CORR) -m $(MARGINS) $(MICRO) -t $* -o $@ $(QR_URL)
