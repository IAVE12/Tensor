import random
import sys
import json
from functools import cmp_to_key


def generate_version_numbers(template):
    versions = []
    for _ in range(2):
        version = []
        for part in template.split('.'):
            if part == '*':
                version.append(str(random.randint(0, 9)))
            else:
                version.append(part)
        versions.append('.'.join(version))
    return versions


def version_compare(v1, v2):
    v1_parts = list(map(int, v1.split('.')))
    v2_parts = list(map(int, v2.split('.')))

    for p1, p2 in zip(v1_parts, v2_parts):
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1

    return 0


def task2(target_version, config_file):
    try:
        with open(config_file) as f:
            config = json.load(f)

        all_versions = []
        for template in config.values():
            all_versions.extend(generate_version_numbers(template))

        sorted_versions = sorted(all_versions, key=cmp_to_key(version_compare))

        print("Отсортированные версии:")
        for version in sorted_versions:
            print(version)

        older_versions = [v for v in all_versions
                          if version_compare(v, target_version) < 0]

        print("\nВерсии старше чем: ", target_version)
        for version in sorted(older_versions, key=cmp_to_key(version_compare)):
            print(version)

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    target_version = sys.argv[1]
    config_file = sys.argv[2]
    task2(target_version, config_file)