project('http-parser', 'c', version : '2.9.3')
install_headers('http_parser.h')
foreach x : [['http_parser',        ['-DHTTP_PARSER_STRICT=0']],
             ['http_parser_strict', ['-DHTTP_PARSER_STRICT=1']]]
  lib = library(x.get(0), 'http_parser.c',
                c_args : x.get(1),
                version : '2.9.3',
                install : true)
  test('test-@0@'.format(x.get(0)),
       executable('test-@0@'.format(x.get(0)), 'test.c',
                  c_args : x.get(1),
                  link_with : lib),
       timeout : 60)	
endforeach