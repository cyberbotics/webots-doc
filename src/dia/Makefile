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
 motor_control.pdf \
 motor_control.pdf.png \
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
 node_hierarchy.pdf \
 node_hierarchy.pdf.png \
 light_sensor.pdf \
 light_sensor.pdf.png \
 physics_execution_scheme.pdf \
 physics_execution_scheme.pdf.png \
 oo_api.pdf \
 oo_api.pdf.png

GUIDE_TARGETS= \
 api_overview.pdf \
 api_overview.pdf.png \
 tutorial_compound_solid.pdf \
 tutorial_compound_solid.pdf.png \
 tutorial_def_use_shape.pdf \
 tutorial_def_use_shape.pdf.png \
 tutorial_feedback_loop.pdf \
 tutorial_feedback_loop.pdf.png \
 tutorial_solid.pdf \
 tutorial_solid.pdf.png \
 tutorial_4_wheels_highlevel.pdf \
 tutorial_4_wheels_highlevel.pdf.png \
 tutorial_4_wheels_lowlevel.pdf  \
 tutorial_4_wheels_lowlevel.pdf.png  \
 controller_plugin.pdf \
 controller_plugin.pdf.png

all : $(REF_TARGETS) $(GUIDE_TARGETS)

%.pdf : %.eps
	epstopdf --outfile=$@ $<

%.eps : %.dia
	dia -e $@ $<

%.pdf.png : %.eps
	convert $< $@

clean :
	rm -f *.pdf *.eps *.png *.dia~ *.log
