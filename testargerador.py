from eos_name_generator import RandomNameGenerator

if __name__ == '__main__':
    generator = RandomNameGenerator()
    names = generator.generate_list(num=1000)
    
    for name in names:
        print(name)