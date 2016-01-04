from scout.ext.backend.utils.get_gene_panels import get_genes


gene_list_lines = [
    "##Database=<ID=gene_list_test.txt,Version=0.1,Date=20151120,Acronym="\
    "FullList,Complete_name=Test List,Clinical_db_genome_build=GRCh37.p13",
    "##Database=<ID=gene_list_test.txt,Version=0.1,Date=20151119,Acronym="\
    "Panel1,Complete_name=Panel1,Clinical_db_genome_build=GRCh37.p13",
    "##Database=<ID=gene_list_test.txt,Version=0.1,Date=20151119,Acronym="\
    "Panel2,Complete_name=Panel2,Clinical_db_genome_build=GRCh37.p13",
     "#Chromosome	Gene_start	Gene_stop	HGNC_symbol	Protein_name	Symptoms"\
     "	Biochemistry	Imaging	Disease_trivial_name	Trivial_name_short"\
     "	Phenotypic_disease_model	OMIM_morbid	Gene_locus	UniProt_id"\
     "	Ensembl_gene_id	Ensemble_transcript_ID	Reduced_penetrance"\
     "	Clinical_db_gene_annotation	Disease_associated_transcript	"\
     "Ensembl_transcript_to_refseq_transcript	Gene_description"\
     "	Genetic_disease_model",
    "19	50887461	50921273	POLD1							POLD1:615381>AD|612591	POLD1:174761"\
    "	19q13.33		ENSG00000062822			Panel1,FullList		POLD1:ENST00000440232"\
    ">NM_001256849/NM_002691|ENST00000593407|ENST00000593887|ENST00000593981|"\
    "ENST00000595904>XM_005259006/XM_005259007|ENST00000596221|ENST00000596425"\
    "|ENST00000596648|ENST00000597963|ENST00000599857|ENST00000600746|ENST00000600859"\
    "|ENST00000601098	POLD1:polymerase_(DNA_directed)__delta_1__catalytic_subunit	",
    "X	16857406	16888537	RBBP7								RBBP7:300825"\
    "	Xp22.2		ENSG00000102054			Panel2,FullList		RBBP7:"\
    "ENST00000330735|ENST00000380084>NM_001198719|ENST00000380087|ENST00000404022>"\
    "NM_002893/XM_005274572|ENST00000416035|ENST00000425696|ENST00000444437"\
    "|ENST00000465244|ENST00000468092|ENST00000481586|ENST00000486166|"\
    "ENST00000493145	RBBP7:retinoblastoma_binding_protein_7	",
    "1	245014468	245027844	HNRNPU								HNRNPU:602869"\
    "	1q44		ENSG00000153187			FullList,Panel2	HNRNPU:NM_031844"\
    "	HNRNPU:ENST00000283179|ENST00000366525|ENST00000440865|ENST00000444376"\
    ">NM_004501/NM_031844|ENST00000465881|ENST00000468690|ENST00000476241"\
    "|ENST00000483966	HNRNPU:heterogeneous_nuclear_ribonucleoprotein_U_(scaffold_attachment_factor_A)	",
    "Y	2654896	2655740	SRY							SRY:400044|400045"\
    "	SRY:480000	Yp11.2		ENSG00000184895			FullList,Panel1"\
    "		SRY:ENST00000383070>NM_003140|ENST00000525526|ENST00000534739"\
    "	SRY:sex_determining_region_Y	", 
    "1	169433147	169455241	SLC19A2							SLC19A2"\
    ":249270>AR	SLC19A2:603941	1q24.2		ENSG00000117479			Panel1"\
    ",FullList,Panel2	SLC19A2:NM_006996.2	SLC19A2:ENST00000236137>NM_006996"\
    "|ENST00000367804>XM_005244840	SLC19A2:solute_carrier_family_19_("\
    "thiamine_transporter)__member_2	",
    "12	58141510	58149796	CDK4							CDK4"\
    ":609048	CDK4:123829	12q14.1		ENSG00000135446			Panel2"\
    ",FullList		CDK4:ENST00000257904>NM_000075|ENST00000312990|"\
    "ENST00000540325|ENST00000546489|ENST00000547281|ENST00000547853|"\
    "ENST00000549606|ENST00000550419|ENST00000551706|ENST00000551800|"\
    "ENST00000551888|ENST00000552254|ENST00000552388|ENST00000552713"\
    "|ENST00000552862|ENST00000553237	CDK4:cyclin-dependent_kinase_4	"
    
]


def test_get_full_list_genes():
    
    genes = get_genes(gene_list_lines, 'FullList')
    assert len(genes) == 6
    assert set(genes) == set(['POLD1', 'RBBP7', 'HNRNPU', 'SRY', 
                                        'SLC19A2', 'CDK4'])

def test_get_panel_1_genes():
    
    genes = get_genes(gene_list_lines, 'Panel1')
    assert len(genes) == 3
    assert set(genes) == set(['POLD1', 'SRY', 'SLC19A2'])

def test_get_panel_2_genes():
    
    genes = get_genes(gene_list_lines, 'Panel2')
    assert len(genes) == 4
    assert set(genes) == set(['RBBP7', 'HNRNPU', 'SLC19A2', 'CDK4'])
