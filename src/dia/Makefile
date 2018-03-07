# Convert .dia into both .pdf and .pdf.png
# for Webots documentation
# written by yvan.bourquin@epfl.ch

REF_TARGETS= \
 ray_orbits.pdf \
 ray_orbits.pdf.png \
 hinge_joint.pdf \
 hinge_joint.pdf.png \
 linear_motor.pdf \
 linear_motor.pdf.png \
 rotational_motor.pdf \
 rotational_motor.pdf.png \
 connector_alignment.pdf \
 connector_alignment.pdf.png \
 emitter_receiver.pdf \
 emitter_receiver.pdf.png \
 receiver_queue.pdf \
 receiver_queue.pdf.png \
 slider_joint.pdf \
 slider_joint.pdf.png \
 light_sensor.pdf \
 light_sensor.pdf.png \
 oo_api.pdf \
 oo_api.pdf.png

all : $(REF_TARGETS)

%.pdf : %.eps
	epstopdf --outfile=$@ $<

%.eps : %.dia
	dia -e $@ $<

%.pdf.png : %.eps
	convert $< $@

clean :
	rm -f *.pdf *.eps *.png *.dia~ *.log
