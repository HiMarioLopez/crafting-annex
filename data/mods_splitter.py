import json
from collections import defaultdict
import os

def split_json_by_domain(input_file, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the massive JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Group entries by their Domain value
    domain_dict = defaultdict(list)
    for entry in data:
        domain = entry.get('Domain')
        if domain is not None:
            domain_dict[domain].append(entry)
    
    # Define the mapping of domain to file names
    domain_to_filename = {
        1: "1_item_mods.json",
        2: "2_flask_mods.json",
        3: "3_monster_mods.json",
        4: "4_strongbox_mods.json",
        5: "5_map_mods.json",
        7: "7_sanctum_arena_relic_mods.json",
        9: "9_bench_mods.json",
        10: "10_base_jewel_mods.json",
        11: "11_compass_mods.json",
        12: "12_leaguestone_mods.json",
        13: "13_abyss_jewel_mods.json",
        14: "14_scarab_mods.json",
        15: "15_dummy_mods.json",
        16: "16_delve_item_mods.json",
        17: "17_delve_map_mods.json",
        18: "18_synthesis_map_mods.json",
        19: "19_synthesis_map_mods.json",
        20: "20_synthesis_map_mods.json",
        21: "21_cluster_jewel_mods.json",
        22: "22_heist_contract_mods.json",
        23: "23_heist_gear_mods.json",
        24: "24_heist_trinket_mods.json",
        25: "25_atlas_watchstone_mods.json",
        26: "26_betrayal_dropped_veiled_mods.json",
        27: "27_expedition_remnant_mods.json",
        28: "28_betrayal_orb_veiled_mods.json",
        29: "29_map_altar_mods.json",
        30: "30_sentinel_mods.json",
        31: "31_atlas_memory_mods.json",
        32: "32_sanctum_player_relic_mods.json",
        33: "33_crucible_map_mods.json",
        34: "34_affliction_tincture_mods.json",
        35: "35_affliction_charm_mods.json",
        36: "36_necropolis_mods.json",
        37: "37_t17_map_mods.json",
    }
    
    # Write each group to the corresponding file
    for domain, entries in domain_dict.items():
        filename = domain_to_filename.get(domain)
        if filename:
            output_file = os.path.join(output_dir, filename)
            with open(output_file, 'w') as outfile:
                json.dump(entries, outfile, indent=4)
    
    print(f"Data successfully split and saved into the 'mods' directory.")

# Example usage:
input_file = 'mods.json'  # Replace with your actual file path
output_dir = 'split_files/mods'   # Directory to save the split files

split_json_by_domain(input_file, output_dir)
