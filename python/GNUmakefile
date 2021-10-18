SHELL = bash
MAKEFILE_ROOT := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

ARTIFACT_OUT_DIR := $(MAKEFILE_ROOT)/../dist/python

START_TASK = @echo -e "\033[0;32m==> $(1)...\033[0m"
START_TARGET = @echo -e "\033[0;35m==> Started target '$@'\033[0m"
DONE_TARGET = @echo -e "\033[0;35m==> Completed target '$@'\033[0m"

.PHONY: bootstrap
bootstrap:
	$(call START_TARGET)
	$(call START_TASK,Ensuring pipenv is configured)
	pipenv install -d
	$(call DONE_TARGET)

.PHONY: test
test:
	$(call START_TARGET)
	$(call START_TASK,Running Python unit tests)
	pipenv run python -m unittest -v $(MAKEFILE_ROOT)/tests/test_*.py
	$(call DONE_TARGET)

.PHONY: lint
lint:
	$(call START_TARGET)
	$(call START_TASK,Linting Python code)
	pipenv run pylint --rcfile $(MAKEFILE_ROOT)/.pylintrc $(MAKEFILE_ROOT)/pulumiup_k8s		
	$(call DONE_TARGET)

.PHONY: package
package:
	$(call START_TARGET)
	$(call START_TASK,Copying README.md and license...)
	cp $(MAKEFILE_ROOT)/../LICENSE $(MAKEFILE_ROOT)
	cp $(MAKEFILE_ROOT)/../README.md $(MAKEFILE_ROOT)
	$(call START_TASK,Building source distribution for Python package...)
	rm -rf $(ARTIFACT_OUT_DIR)
	mkdir -p $(ARTIFACT_OUT_DIR)
	pipenv run python $(MAKEFILE_ROOT)/setup.py sdist \
		--dist-dir $(ARTIFACT_OUT_DIR)
	$(call START_TASK,Removing copied files...)
	rm -f $(MAKEFILE_ROOT)/LICENSE $(MAKEFILE_ROOT)/README.rst
	$(call DONE_TARGET)


.PHONY: publish
publish:
	$(call START_TARGET)
	$(call START_TASK,Publishing module...)
	pipenv run python -m twine upload $(ARTIFACT_OUT_DIR)/**
	$(call DONE_TARGET)
