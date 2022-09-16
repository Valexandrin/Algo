import re
from typing import List


def modify_name(origin_name: str) -> list:
    res = re.split('\W+', origin_name)
    res = [item for item in res if item]
    return res


def get_match(asset: List[str], material: List[str], match_level: int) -> dict:
    match_level = match_level/100
    matches = {}
    for a in asset:
        if not a or a in matches:
            continue

        for m in material:
            if not m or m in matches:
                continue
            longest, sub_len = max(len(a), len(m)), 0            

            while sub_len < min(len(a), len(m)):
                if a[sub_len] == m[sub_len]:                    
                    sub_len += 1                    
                else:
                    break
            
            if sub_len/longest > match_level:                
                matches[a[0:sub_len]] = sub_len/longest
    
    return matches


def count_level(asset: List[str], material: List[str], matches: dict) -> float:
    matches_mean = sum(matches.values()) / len(matches.values())

    asset_match = len(matches) / len(asset)
    material_match = len(matches) / len(material)
    matches_usage = (asset_match + material_match) / 2

    total_matches = 100 * matches_mean * matches_usage

    return round(total_matches, 2)


def heaps_comparison(assets: List[str], materials: List[str], target_match_level: int):
    for asset in assets:
        asset = modify_name(asset)
        for material in materials:
            material = modify_name(material)
            actual_match_level = 0

            matches = get_match(asset, material, target_match_level)
            if matches:
                actual_match_level = count_level(asset, material, matches)

            if actual_match_level >= target_match_level:                                
                print(
                    '---\
                    \nAsset: {asset}\
                    \nMaterial: {material}\
                    \nMatch level: {level}\
                    \nMatches: {matches}'.format(
                    asset = asset,
                    material = material,                
                    level = actual_match_level,
                    matches = list(matches.keys()),
                    )
                )


def main():
    target_match_level = 50
    assets = ['палатка каркасная ПК -10 камуфлированной расцветки', 'палатка каркасная(ПК- 10)']
    materials = ['палатка', 'полотно', 'каркас для палатки', 'пожарный кран ПК -10']

    heaps_comparison(assets, materials, target_match_level)


if __name__ == '__main__':
    main()
