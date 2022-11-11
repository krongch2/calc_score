%% 1. Import SHAPE data. 
% Select the SHAPE reactivity only on the PTC regions and exclude any hairpins
reactivity = d_SHAPE(24:307);
%% 2. Define secondary structure of RNA structure
% Define pair and unpaired nucleotides, X = paired and . = unpaired. 
% Create string represents the secondary structure information
structure = "XXXXXXXX.XXX.XX......XXXX.XXXXXX..XXXXX.XXX.XXXXX....XXXXX.XXX..XXXXX..XXX.......XXX.........XXXX..XXXXXX........XXX...XXXXXX...XX.......XX...XXXXXX....XXX.........XXXXX..XXXXX..XXXXXXXXX......XXXXXX..XXX.XXXXX.....XXXXX.....XXXXX......XXX.XX....XXXXXXX....XXX.XXXX....XX..XXXXXXXXXXX";
% Convert string to array. Append this array to reactivity



%% 3. Define threshold and score
% For each nucleotide, if it is X and has reactivity < 0.5 then score = +1
% if it is . and has reactivity > 0.25 then score = +1
% Else score = 0


%% 4. Calculate SHAPE score as percentage
% Score/Length of nucleotide 

SHAPE_score = score/284; 

