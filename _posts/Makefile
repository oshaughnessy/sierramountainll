DATESTAMP=$(shell date +%Y-%m-%d)

%:
	[ ! -f $(DATESTAMP)-$@.md ] && { printf -- "---\ntitle: \ntag: \n---\n\n" >> $(DATESTAMP)-$@.md; } || true
	vim $(DATESTAMP)-$@.md

.PHONY: c commit
c commit:
	git commit -av

.PHONY: p push
p push:
	git push
