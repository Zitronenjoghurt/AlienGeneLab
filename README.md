# AlienGeneLab (work in progress | highly unfinished)
An experiment, trying to find out if alien breeding can be gamified (don't ask).

All aliens have a genotype and a phenotype. 

The genotype will include all loci (pairs of alleles which influence a certain property of the alien). The dominant of the two alleles in a locus will determine the expression of the individual body part property. Usually the allele with the higher value will be the dominant one in a locus. 
e.g.: an alien has a locus for the red, green and blue part of the skin color. Now the red locus (same as all else) has two alleles which can have different values. The dominant (highest) of them will decide how much red the skin color of the alien includes.

The phenotype describes how the organism looks like. To determine the phenotype you analyze the genotype and summarize all effects of every locus. For the color property of a body part you would join the 3 loci (the red, green and blue parts) and translate them into a color. Internally the color will be approximated to the closest one of 135 preconfigured colors (look src/data/colors.json). Depending on the property of a body part, some loci will be analyzed differently to determine the end result.

The nice thing is: you can just add the genes you want to an alien. No gene is actually mandatory and you can easily add your own ones (look src/data/genes.json). The only limitation is the amount of different body part properties genes can influence (since they have to be analyzed depending on the specific situation, like the color genes). You can add whatever body part genes you want and put them in an alien without having to change the python code.

------------------------

# Configuration

## src/config.json
To customize global settings, changing the behaviour of the simulation.

|Property|Type|Description|Default|Values|
|---|---|---|---|---|
|`gene_insertion_chance`|float|The chance for each individual existing gene being inserted into a randomly generated alien.|`0.5`|`0 - 1`|
|`duplicate_differing_alleles`|bool|Enable if alleles should be duplicated if only one of the bred aliens has a certain gene.|`true`||
|`duplicate_differing_alleles_chance`|float|The chance of alleles being duplicated if only one of the bred aliens has a certain gene. Higher values might turn the outcome crazy if the parent aliens are very different.|`0.5`|`0 - 1`|