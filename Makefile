ifndef spec
spec=uuu.spec
endif

srpm:
	rpmdev-setuptree
	@set -e; rpmbuild -bs --define "_disable_source_fetch 0" $(spec)
ifdef outdir
	cp `rpmbuild --eval "%{_topdir}"`/SRPMS/* $(outdir)
endif
