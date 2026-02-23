from typing import (
    Dict,
    List
)
from brs_utils import create_logger
from rplibs import rpPathway
from rplibs.Args import build_args_parser


def counts(pathways: List[rpPathway]) -> Dict:

    # SPECIES
    species_l = [
        pathway.get_species_ids()
        for pathway in pathways
    ]
    species_l = sorted(list(set([y for x in species_l for y in x])))

    # REACTIONS
    reactions_l = []
    for pathway in pathways:
        for rxn in pathway.get_list_of_reactions():
            if rxn not in reactions_l:
                reactions_l += [rxn]

    return {
        'species': species_l,
        'reactions': [rxn.to_string() for rxn in reactions_l]
    }

def print_stats(
    pathways: List[rpPathway],
    species: Dict,
    reactions: Dict
) -> None:

    # PATHWAYS
    title = f'{len(pathways)} Pathway(s)'
    print(title)
    print('='*len(title))
    for pathway in pathways:
        print(f'   - {pathway.get_id()} ({pathway.get_nb_reactions()} reactions, {pathway.get_nb_species()} species)')
    print()

    # SPECIES
    title = f'{len(species)} Species'
    print(title)
    print('='*len(title))
    print(', '.join(species))
    print()

    # REACTIONS
    title = f'{len(reactions)} Reactions'
    print(title)
    print('='*len(title))
    for rxn in reactions:
        print(f'   - {rxn}')
    print()

def entry_point():
  
    parser = build_args_parser(
        prog='stats',
        description='Statistics on SBML file(s)'
    )
    args = parser.parse_args()

    # Create logger
    logger = create_logger(parser.prog, args.log)

    # Build the list of pathways to rank
    pathways = [
        rpPathway(
            infile=pathway_filename,
            logger=logger
        ) for pathway_filename in args.pathways
    ]

    # Rank pathways
    stats = counts(pathways)

    print_stats(
        pathways=pathways,
        reactions=stats['reactions'],
        species=stats['species'],
        )

if __name__ == '__main__':
    entry_point()
