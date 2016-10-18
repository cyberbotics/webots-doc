.PHONY: dia
.PHONY: math

default:
	@echo "Type one of the following:"
	@echo "  make dia                   for the diagrams"
	@echo "  make math                  for the math formulas"
	@echo "  make clean                 remove useless files"

dia: dia/*.dia
	@echo "Producing diagrams..."
	@make install -C dia

math: math/*.tex
	@echo "Producing math formulas..."
	@make install -C math

clean:
	@make clean -C math
	@make clean -C dia
