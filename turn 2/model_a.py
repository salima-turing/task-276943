from typing import Any, List, Optional
import third_party_lib

# Using a type stub for a third-party library
import third_party_lib_stub  # Provides type definitions for third_party_lib

def process_data(data: List[Any]) -> List[str]:
	results: List[str] = []
	for item in data:
		if isinstance(item, str):
			results.append(item.upper())
	return results

def use_third_party_func(arg: int) -> Optional[str]:
	return third_party_lib.some_func(arg)  # mypy will check based on third_party_lib_stub

if __name__ == "__main__":
	data = [1, "two", 3.0, "four"]
	processed_data = process_data(data)
	print(processed_data)

	result = use_third_party_func(5)
	if result:
		print(result.upper())
