# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase

import inol_rest.api.core as core
import inol_rest.inol_calc.calculator as calc

# Create your tests here.

class CalculatorTestCase(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        #we dont need to do anything here
    
    def test_calculate_excercise_inol(self):
        reps = 2
        sets = 6
        weight = 100
        current_max = 125
        self.assertEqual(calc.calculate_excercise_inol(reps,weight,current_max,sets), 0.6000000000000001)
    
    def test_calculate_inol(self):
        reps = 6
        intensity = 80

        self.assertEqual(calc.calculate_inol(reps,intensity), 0.3)


    def test_calculate_inol_100(self):
        reps = 1
        intensity = 100

        self.assertEqual(calc.calculate_inol(reps,intensity), 99.99999999994884)

    def test_calculate_inol_101(self):
        reps = 1
        intensity = 101

        self.assertEqual(calc.calculate_inol(reps,intensity), -1)
 
    
    def test_calculate_set_inol(self):
        reps = 6
        weight = 100
        current_max = 125
        self.assertEqual(calc.calculate_set_inol(reps,weight,current_max), 0.3)
    
    def test_calculate_set_inol_at_rep_max(self):
        reps = 1
        weight = 100
        current_max = 100
        self.assertEqual(calc.calculate_set_inol(reps,weight,current_max), 2.0100000000000215)
    
    def test_calculate_set_inol_above_rep_max(self):
        reps = 1
        weight = 110
        current_max = 100
        self.assertEqual(calc.calculate_set_inol(reps,weight,current_max), 2.210000000000008)



    def test_eftsrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.eftsrm(reps,weight), 133)

    def test_lomrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.lomrm(reps,weight), 125)

    def test_brzrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.brzrm(reps,weight), 133)
 
    def test_eplrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.eplrm(reps,weight), 133)
 
    def test_mayrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.mayrm(reps,weight), 130)
         
    def test_ocorm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.ocorm(reps,weight), 125)
 
    def test_watrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.watrm(reps,weight), 134)
         
    def test_lanrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.lanrm(reps,weight), 134)
         
    def test_avgrm(self):
        reps = 10
        weight = 100
        self.assertEqual(calc.avgrm(reps,weight), 130)
    
    def test_lomrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.lomrm(reps,weight), 100)

    def test_brzrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.brzrm(reps,weight), 100)
 
    def test_eplrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.eplrm(reps,weight), 103)
 
    def test_mayrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.mayrm(reps,weight), 108)
         
    def test_ocorm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.ocorm(reps,weight), 102)
 
    def test_watrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.watrm(reps,weight), 101)
         
    def test_lanrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.lanrm(reps,weight), 101)
         
    def test_avgrm_1rep(self):
        reps = 1
        weight = 100
        self.assertEqual(calc.avgrm(reps,weight), 102)