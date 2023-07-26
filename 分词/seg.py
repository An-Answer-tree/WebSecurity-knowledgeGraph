import pkuseg


if __name__ == '__main__':
    pkuseg.test('input.txt', 'result.txt', model_name='web',postag=True, nthread=20)

