import re
from typing import List
import time

cache = set()


def modify_name(origin_name: str) -> list:
    res = re.split('\W+', origin_name)
    res = [item for item in res if item]
    return res


def sub_measure(s1: str, s2: str) -> int:    
    len1, len2 = len(s1), len(s2)

    if s1 == s2 and s1 in cache:                
        return min(len1, len2)        
    
    sub_len = 0
    while sub_len < min(len1, len2):
        if s1[sub_len] == s2[sub_len]:                    
            sub_len += 1
        else:
            return sub_len

    return sub_len


def get_match(asset: List[str], material: List[str], target_match_level: int) -> dict:
    target_match_level = target_match_level/100
    matches = {}
    for a in asset:
        if a in matches:
            continue

        for m in material:
            if m in matches:
                continue
            
            sub_len = sub_measure(a, m)            
            match = a[0:sub_len]
            cache.add(match)

            match_level = sub_len / max(len(a), len(m))

            if match_level > target_match_level:                
                matches[match] = match_level
    
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
    start = time.time()
    target_match_level = 50
    assets = ['палатка каркасная ПК -10 камуфлированной расцветки ', 'палатка каркасная(ПК- 10)']
    materials = ['палатка', 'полотно', 'каркас для палатки', 'пожарный кран ПК -10']

    heaps_comparison(assets, materials, target_match_level)
    print(f'\nTotal time: {time.time() - start}')


if __name__ == '__main__':
    main()
