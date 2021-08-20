function hexXor(param) {
            var ret = '';
            for (var i = 0; i < this['length'] && i < param['length']; i += 2) {
                var a = parseInt(this['slice'](i, i + 2), 10);
                var b = parseInt(param['slice'](i, i + 2), 10);
                var c = (a ^ b)['toString'](10);
                if (c['length'] == 1) {
                    c = '0' + c;
                }
                ret += c;
            }
            return ret;
        }
