#! /usr/bin/env sh
echo "#############################"
echo "#### Running e2e tests!! ####"
echo "#############################"
echo ""

count=0 # number of test cases run so far

for test in tests_e2e/*.in; do
    name=$(basename $test .in)
    expected=tests_e2e/$name.out
    
    # Run all e2e test cases using files found in the tests_e2e folder
    python3 run.py board_e2e_test.txt< $test | diff - $expected || echo "Test $name: failed!"

    count=$((count+1))
done

echo "Finished running $count tests!"
echo ""
