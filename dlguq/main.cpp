#include <iostream>
#include <fstream>
#include <string>
#include <string_view>
#include "aho_corasick.hpp"

using namespace std;

bool   g_print = false;
string g_input_str;
string g_input_path;
string g_output_str;
string g_output_path;
string g_filter_path;

size_t strlen_utf8(string_view str)
{
	size_t length = 0;
	for (size_t i = 0; i < str.size();) {
		length++;

		auto byte = str[i];
		if (!(byte & 0b10000000)) i += 1;
		else if (!(byte & 0b01000000)) i += 2;
		else if (!(byte & 0b00100000)) i += 3;
		else i += 4;
	}

	return length;
}

void print_help()
{
	const char* help_message = R"(
[Input Options]
	"[string]" set input string
	-i [path]  set input file path
	-f [path]  set filter file path

[Output Options]
	-o [path]  set output file path
	-p         print result

	-h help
)";
	cout << help_message;
}

int main(int argc, const char* argv[])
{
	for (int i = 1; i < argc;) {
		string arg = argv[i];

		if (arg[0] == '"') {
			string_view sv(argv[i]);
			auto first = sv.find_first_of('"') + 1;
			auto last = sv.find_last_of('"');
			g_input_str = sv.substr(first, last - first - 1);
			i += 1;
		} else if (arg == "-p") {
			g_print = true;
			i += 1;
		} else if (arg == "-i") {
			if (argc < i + 2) return -1;
			g_input_path = argv[i + 1];
			i += 2;
		} else if (arg == "-o") {
			if (argc < i + 2) return -1;
			g_output_path = argv[i + 1];
			i += 2;
		} else if (arg == "-f") {
			if (argc < i + 2) return -1;
			g_filter_path = argv[i + 1];
			i += 2;
		} else if (arg == "-h") {
			print_help();
			return 0;
		} else {
			print_help();
			return -1;
		}
	}

	if (g_input_str.empty()) {
		ifstream file(g_input_path);

		file.seekg(0, std::ios::end);
		g_input_str.resize(file.tellg());
		file.seekg(0);
		file.read(&g_input_str[0], g_input_str.size());
	} else {
		return -1;
	}

	aho_corasick::trie trie;
	if (!g_filter_path.empty()) {
		ifstream file(g_filter_path);
		string str;

		while (getline(file, str))
			trie.insert(str);
	} else {
		return -1;
	}

	trie.remove_overlaps();
	auto result = trie.parse_text(g_input_str);

	if (!result.empty()) {
		g_output_str += g_input_str.substr(0, result.front().get_start());
		for (size_t i = 0; i < result.size(); ++i) {
			size_t censor_size = strlen_utf8(result[i].get_keyword());
			while (censor_size-- > 0) g_output_str += '*';

			if (i + 1 == result.size()) break;

			g_output_str += g_input_str.substr(result[i].get_end() + 1, result[i + 1].get_start() - result[i].get_end() - 1);
		}
		g_output_str += g_input_str.substr(result.back().get_end() + 1);
	}

	if (g_print)
		cout << g_output_str << endl;

	if (!g_output_path.empty()) {
		ofstream file(g_output_path);
		file << g_output_str;
	}

	return 0;
}