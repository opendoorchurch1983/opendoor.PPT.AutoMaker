from AutoMaker import AutoMaker

if __name__ == '__main__':
    inputs = input().split(',')
    automaker = AutoMaker()
    automaker.CopyAndPaste(inputs)
    automaker.SaveAsPPTX('result')
