# Convert .svg into both .pdf and .pdf.png
# for Webots documentation
# written by luc.guyot@epfl.ch

REF_TARGETS= \
 sonar_reflection.pdf \
 sonar_reflection.pdf.png \
 propeller.pdf \
 propeller.pdf.png \

all : $(REF_TARGETS)

%.pdf : %.svg
	inkscape --export-pdf $@ $<

%.pdf.png : %.svg
	inkscape --export-png $@ $<

clean :
	rm -f *.pdf *.png *.svg~ *.log
