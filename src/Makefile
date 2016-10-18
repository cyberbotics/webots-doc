.PHONY: dia
.PHONY: tex

default:
	@echo "Type one of the following:"
	@echo "  make dia                   for the diagrams"
	@echo "  make tex                   for the math formulas"
	@echo "  make clean                 remove useless files"

dia: dia/*.dia
	@echo "Producing diagrams..."
	@make install -C dia

tex: tex/*.tex
	@echo "Producing math formulas..."
	@make install -C tex

clean:
	@make clean -C tex
	@make clean -C dia
