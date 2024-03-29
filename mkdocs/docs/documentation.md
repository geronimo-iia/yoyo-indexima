# Documentation 

Note on documentation generation.

## Tooling

- mkdocs to generate web site
- pydocmd (based on mkdocs) to generate API doc from docstyle
- pyreverse to generate uml diagram

## Documentation folder

under mkdocs folder:

- 'docs' which keep handle writed doc file,
- 'docs/api' api generated files folder
- 'docs/uml' uml gererated diagrams folder
-  'mkdocs.yaml': configuration file for mkdocs tool

## Makefile targets


Main target: 'docs'

- call 'mkdocs-site':
    - call 'mkdocs-md': Copy standard document
    - Build web site with mkdocs tool
    - move generated website content into '/docs' folder in order to expose with github page project

Cleaning target: '.clean-docs'
- Remove all temp files
    

## Extract from Makefile

```


DOCS_PATH := mkdocs/docs
SITE_PATH := mkdocs/site


MK_FILES = $(DOCS_PATH)/index.md $(DOCS_PATH)/license.md $(DOCS_PATH)/changelog.md $(DOCS_PATH)/code_of_conduct.md

mkdocs-md: $(MK_FILES) # Copy standard document
$(DOCS_PATH)/index.md: README.md
	@ cp -f README.md $(DOCS_PATH)/index.md
$(DOCS_PATH)/license.md: LICENSE.md
	@ cp -f LICENSE.md $(DOCS_PATH)/license.md
$(DOCS_PATH)/changelog.md: CHANGELOG.md
	@ cp -f CHANGELOG.md $(DOCS_PATH)/changelog.md
$(DOCS_PATH)/code_of_conduct.md: CODE_OF_CONDUCT.md
	@ cp -f CODE_OF_CONDUCT.md $(DOCS_PATH)/code_of_conduct.md

mkdocs-site: mkdocs/mkdocs.yml mkdocs-md ## Build Documentation Site
	@ cd mkdocs; \
	  $(RUN) mkdocs build
	@ rm -rf docs/
	@ mv mkdocs/site docs/	

.clean-docs: ## remove all generated files
	@ rm -rf mkdocs/site
	@ rm -rf $(DOCS_PATH)/uml
	@ rm -rf $(DOCS_PATH)/api
	@ rm -rf $(DOCS_PATH)/index.md
	@ rm -rf $(DOCS_PATH)/license.md
	@ rm -rf $(DOCS_PATH)/changelog.md
	@ rm -rf $(DOCS_PATH)/code_of_conduct.md

docs: mkdocs-site ## Generate documentation and UML
```
