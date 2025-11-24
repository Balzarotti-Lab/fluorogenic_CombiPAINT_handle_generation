# fluorogenic_CombiPAINT_handle_generation
Repository of scripts for the de novo generation of mismatching (fluorogenic) combinatorial DNA-PAINT multiplexing (Combi-PAINT) handles and imagers. 

"15_nt_handle_design_biopython.ipynb" is the code that, following the mathematical model and using BioPython functions, randomly generates a candidate set and checks if it passes quality checks. Candidate sets and their matrix of binding energies are saved in a .txt file and can be inspected and analyzed to choose best candidates.

"brute_force_handles_X.py" are the programs that check all handles whose second nucleotide is X (first and last nucleotides are always fixed). Each program can be run on a separate unit, and takes (Intel Xeon Gold 6138) ~9 hours to run. They generate "handles_X.txt" files.

"brute_forcing_analysis.ipynb" is the notebook that takes all "handles_X.txt" files, adds other data (self-binding energy, uniformity of binding energies, etc.) and makes a full .csv file with the data. This can be filtered and further analysed in the same notebook to make shortlists of handles.
