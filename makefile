PACKAGE = senkalib-0.2.4

.PHONY: build-package
build-package:
	poetry build
	tar zxvf dist/$(PACKAGE).tar.gz -C ./dist
	cp dist/$(PACKAGE)/setup.py setup.py
	rm -rf dist