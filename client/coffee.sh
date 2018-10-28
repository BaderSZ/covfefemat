#!/bin/bash

call(){
  ## call functions
  curl -X $(echo $2 | tr [:lower:] [:upper:]) -I $1;

  return 0;
}

help(){
  ## print help
  echo -e \
	"\t ____ ____ _  _ ____ ____ ____ ____ _  _ ____ ___\n"        \
	"\t |___ [__]  \\/  |--- |=== |--- |=== |\/| |--|  | \n\n"     \
          "\tBrought to you by Bader. I am not responsible in\n" \
          "\tcase your coffeemaker burns down. Blame the Juju\n" \
          "\tin the mountain or my loud upstairs neighbours.\n\n"\
          "\tSyntax: <command> <address> <request>\n"            \
          "\tExample: coffee.sh coffee.localhost BREW\n"

  return 0;
}

case $1 in
  help|""|-h)
      help;
      ;;
  *)
      call $1 $2;
      ;;
esac;

