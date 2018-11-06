"""
    
"""
import math


def main():
    data = Data.getWaterMelonData()
    label = Data.getWaterMelonLabel()
    
    root = build_decision_tree(data,label)
    


if __name__ == '__main__':
    main()
