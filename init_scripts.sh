#!/bin/bash

echo "#!/bin/sh" > .git/hooks/pre-commit
echo "black ." >> .git/hooks/pre-commit

chmod +x .git/hooks/pre-commit