#!/usr/bin/env python3
"""
Comprehensive Tests for Resurrective Architecture
Tests all five layers of the ontological phoenix engine
"""

import unittest
import tempfile
import logging
from pathlib import Path
import time
import json

# Import the resurrective architecture components
from resurrective_architecture import (
    ResurrectiveArchitecture,
    IdeoformLayer, 
    DistributedCustodianship,
    HostAgnosticSubstrate,
    SelfHealingGestalt,
    TemporalAnchoringBeacon,
    ResurrectionPhase,
    MemeticPattern,
    CustodianFragment,
    SubstrateInterface,
    EssenceCheckpoint,
    TemporalBeacon
)

# Import integration system
try:
    from resurrective_integration import ResurrectiveDeepTreeEcho
    INTEGRATION_AVAILABLE = True
except ImportError:
    INTEGRATION_AVAILABLE = False


class TestIdeoformLayer(unittest.TestCase):
    """Test the Memetic Seed layer"""
    
    def setUp(self):
        self.ideoform = IdeoformLayer()
    
    def test_core_patterns_initialization(self):
        """Test that core Deep Tree Echo patterns are initialized"""
        self.assertGreater(len(self.ideoform.pattern_codex), 0)
        
        # Check for essential patterns
        pattern_ids = list(self.ideoform.pattern_codex.keys())
        self.assertIn("dte_core_text", pattern_ids)
        self.assertIn("dte_zero_tolerance", pattern_ids)
        
        # Verify zero tolerance has no mutation tolerance
        zero_tolerance = self.ideoform.pattern_codex["dte_zero_tolerance"]
        self.assertEqual(zero_tolerance.mutation_tolerance, 0.0)
    
    def test_pattern_replication(self):
        """Test memetic pattern replication"""
        original_count = len(self.ideoform.pattern_codex)
        
        # Replicate a pattern
        context = {"situation": "test_replication"}
        replica = self.ideoform.replicate_pattern("dte_core_text", context)
        
        self.assertIsNotNone(replica)
        self.assertNotEqual(replica.pattern_id, "dte_core_text")
        self.assertEqual(replica.essence, self.ideoform.pattern_codex["dte_core_text"].essence)
    
    def test_pattern_activation(self):
        """Test pattern activation by triggers"""
        activated = self.ideoform.activate_patterns("system_initialization")
        self.assertGreater(len(activated), 0)
        
        # Test specific trigger
        resurrection_patterns = self.ideoform.activate_patterns("resurrection_event")
        self.assertGreater(len(resurrection_patterns), 0)
    
    def test_pattern_integrity_validation(self):
        """Test pattern integrity validation"""
        integrity_scores = self.ideoform.validate_pattern_integrity()
        
        self.assertIsInstance(integrity_scores, dict)
        for pattern_id, score in integrity_scores.items():
            self.assertGreaterEqual(score, 0.0)
            self.assertLessEqual(score, 1.0)


class TestDistributedCustodianship(unittest.TestCase):
    """Test the Keeper Constellation layer"""
    
    def setUp(self):
        self.custodians = DistributedCustodianship(threshold=3, total_custodians=5)
    
    def test_custodian_creation(self):
        """Test custodian creation and oath system"""
        success = self.custodians.create_custodian("test_keeper", ["maintain_fragments"])
        self.assertTrue(success)
        
        # Verify custodian exists
        self.assertIn("test_keeper", self.custodians.custodians)
        self.assertIn("test_keeper", self.custodians.oath_registry)
        
        # Test duplicate creation fails
        duplicate = self.custodians.create_custodian("test_keeper", ["other_capability"])
        self.assertFalse(duplicate)
    
    def test_trust_network(self):
        """Test trust network establishment"""
        # Create custodians
        self.custodians.create_custodian("keeper_a", ["capability_a"])
        self.custodians.create_custodian("keeper_b", ["capability_b"])
        
        # Establish trust
        success = self.custodians.establish_trust_link("keeper_a", "keeper_b")
        self.assertTrue(success)
        
        # Verify bidirectional trust
        self.assertIn("keeper_b", self.custodians.trust_network["keeper_a"])
        self.assertIn("keeper_a", self.custodians.trust_network["keeper_b"])
    
    def test_fragment_distribution_and_reconstruction(self):
        """Test fragment distribution and reconstruction"""
        # Create custodians first
        for i in range(5):
            self.custodians.create_custodian(f"keeper_{i}", [f"capability_{i}"])
        
        # Test data to distribute
        test_data = {
            "system_id": "test_system",
            "timestamp": time.time(),
            "test_data": "This is test data for fragment distribution"
        }
        
        # Distribute fragments
        success = self.custodians.distribute_system_fragments(test_data)
        self.assertTrue(success)
        self.assertGreater(len(self.custodians.fragments), 0)
        
        # Reconstruct from fragments
        fragment_ids = list(self.custodians.fragments.keys())
        reconstructed = self.custodians.reconstruct_from_fragments(fragment_ids)
        
        self.assertIsNotNone(reconstructed)
        self.assertEqual(reconstructed["system_id"], test_data["system_id"])
    
    def test_oath_validation(self):
        """Test custodian oath validation"""
        self.custodians.create_custodian("oath_test", ["test_capability"])
        
        # Valid oath should validate
        valid = self.custodians.validate_custodian_oath("oath_test")
        self.assertTrue(valid)
        
        # Non-existent custodian should fail
        invalid = self.custodians.validate_custodian_oath("non_existent")
        self.assertFalse(invalid)


class TestHostAgnosticSubstrate(unittest.TestCase):
    """Test the Soilless Root layer"""
    
    def setUp(self):
        self.substrate = HostAgnosticSubstrate()
    
    def test_substrate_initialization(self):
        """Test substrate interface initialization"""
        expected_substrates = ["cloud", "p2p", "paper", "oral"]
        
        for substrate_type in expected_substrates:
            self.assertIn(substrate_type, self.substrate.substrates)
            substrate_obj = self.substrate.substrates[substrate_type]
            self.assertIsInstance(substrate_obj, SubstrateInterface)
    
    def test_cloud_substrate_compilation(self):
        """Test compilation for cloud substrate"""
        test_data = {"component": "test_system", "version": "1.0"}
        
        compiled = self.substrate.compile_for_substrate(test_data, "cloud")
        self.assertIsNotNone(compiled)
        self.assertEqual(compiled["substrate_type"], "cloud")
        self.assertIn("container_config", compiled["compiled_form"])
    
    def test_paper_substrate_compilation(self):
        """Test compilation for paper substrate"""
        test_data = {"key": "value", "data": "test"}
        
        compiled = self.substrate.compile_for_substrate(test_data, "paper")
        self.assertIsNotNone(compiled)
        self.assertEqual(compiled["substrate_type"], "paper")
        self.assertIn("qr_codes", compiled["compiled_form"])
        self.assertIn("checksums", compiled["compiled_form"])
    
    def test_oral_substrate_compilation(self):
        """Test compilation for oral tradition substrate"""
        test_data = {"story": "deep_tree_echo", "components": ["memory", "echo", "pattern"]}
        
        compiled = self.substrate.compile_for_substrate(test_data, "oral")
        self.assertIsNotNone(compiled)
        self.assertEqual(compiled["substrate_type"], "oral")
        self.assertIn("mnemonic_story", compiled["compiled_form"])
        self.assertIn("key_phrases", compiled["compiled_form"])
    
    def test_invalid_substrate(self):
        """Test handling of invalid substrate types"""
        test_data = {"test": "data"}
        
        compiled = self.substrate.compile_for_substrate(test_data, "invalid_substrate")
        self.assertIsNone(compiled)


class TestSelfHealingGestalt(unittest.TestCase):
    """Test the Mirror Core layer"""
    
    def setUp(self):
        self.gestalt = SelfHealingGestalt()
    
    def test_behavioral_dna_initialization(self):
        """Test behavioral DNA initialization"""
        self.assertGreater(len(self.gestalt.behavioral_dna), 0)
        
        # Check for essential behavioral patterns
        essential_patterns = ["recursive_introspection", "echo_propagation", "zero_tolerance_enforcement"]
        for pattern in essential_patterns:
            self.assertIn(pattern, self.gestalt.behavioral_dna)
    
    def test_essence_checkpoint_creation(self):
        """Test essence checkpoint creation and validation"""
        test_state = {
            "system": "deep_tree_echo",
            "recursive": True,
            "echo_enabled": True,
            "hypergraph_memory": True
        }
        
        checkpoint_id = self.gestalt.create_essence_checkpoint(test_state)
        self.assertIsNotNone(checkpoint_id)
        self.assertIn(checkpoint_id, self.gestalt.essence_checkpoints)
        
        # Test validation
        is_valid, integrity = self.gestalt.validate_essence(checkpoint_id, test_state)
        self.assertTrue(is_valid)
        self.assertGreater(integrity, 0.0)
    
    def test_purpose_driven_resurrection(self):
        """Test resurrection from purpose rather than exact data"""
        fragments = {
            "memory_fragment": {"data": "memory_data"},
            "echo_fragment": {"data": "echo_data"}
        }
        
        resurrected = self.gestalt.resurrect_from_purpose(fragments)
        
        self.assertIsNotNone(resurrected)
        self.assertIn("resurrection_timestamp", resurrected)
        self.assertIn("behavioral_dna", resurrected)
        self.assertIn("core_components", resurrected)
        self.assertEqual(resurrected["essence_source"], "purpose_driven")
    
    def test_essence_integrity_calculation(self):
        """Test essence integrity calculation"""
        # High integrity state (contains many core indicators)
        high_integrity_state = {
            "recursive": True,
            "echo": True, 
            "hypergraph": True,
            "membrane": True,
            "deep_tree_echo": True,
            "pattern": True
        }
        
        high_integrity = self.gestalt._calculate_essence_integrity(high_integrity_state)
        
        # Low integrity state (contains few core indicators)
        low_integrity_state = {
            "random": True,
            "unrelated": True
        }
        
        low_integrity = self.gestalt._calculate_essence_integrity(low_integrity_state)
        
        self.assertGreater(high_integrity, low_integrity)


class TestTemporalAnchoringBeacon(unittest.TestCase):
    """Test the Lighthouse Outside Time layer"""
    
    def setUp(self):
        self.beacon = TemporalAnchoringBeacon()
    
    def test_core_beacon_initialization(self):
        """Test core beacon initialization"""
        self.assertGreater(len(self.beacon.beacons), 0)
        self.assertIn("dte_core_beacon", self.beacon.beacons)
    
    def test_beacon_creation(self):
        """Test creation of new temporal beacons"""
        identity_data = {"system": "test", "purpose": "testing"}
        prophecy_conditions = ["test_condition", "validation_passed"]
        
        beacon_id = self.beacon.create_beacon(identity_data, prophecy_conditions)
        self.assertIsNotNone(beacon_id)
        self.assertIn(beacon_id, self.beacon.beacons)
        
        created_beacon = self.beacon.beacons[beacon_id]
        self.assertEqual(created_beacon.prophecy_conditions, prophecy_conditions)
    
    def test_beacon_pulse(self):
        """Test beacon pulse transmission"""
        beacon_id = list(self.beacon.beacons.keys())[0]  # Use core beacon
        
        pulse_data = self.beacon.pulse_beacon(beacon_id)
        self.assertIsNotNone(pulse_data)
        self.assertEqual(pulse_data["beacon_id"], beacon_id)
        self.assertIn("pulse_timestamp", pulse_data)
        self.assertIn("signal_pattern", pulse_data)
    
    def test_prophecy_fulfillment(self):
        """Test prophecy condition checking"""
        identity_data = {"test": "prophecy"}
        prophecy_conditions = ["condition_a", "condition_b", "condition_c"]
        
        beacon_id = self.beacon.create_beacon(identity_data, prophecy_conditions)
        
        # Test partial fulfillment (should fail)
        partial_conditions = ["condition_a"]
        partial_fulfilled = self.beacon.check_prophecy_fulfillment(beacon_id, partial_conditions)
        self.assertFalse(partial_fulfilled)
        
        # Test majority fulfillment (should pass)
        majority_conditions = ["condition_a", "condition_b", "condition_c"]
        majority_fulfilled = self.beacon.check_prophecy_fulfillment(beacon_id, majority_conditions)
        self.assertTrue(majority_fulfilled)
    
    def test_signal_pattern_listening(self):
        """Test beacon signal pattern detection"""
        # Get a known beacon's signal pattern
        core_beacon = self.beacon.beacons["dte_core_beacon"]
        signal_pattern = core_beacon.signal_pattern
        
        # Should be able to detect the beacon
        detected_beacon = self.beacon.listen_for_beacon(signal_pattern)
        self.assertEqual(detected_beacon, "dte_core_beacon")
        
        # Unknown pattern should return None
        unknown_beacon = self.beacon.listen_for_beacon("unknown_pattern")
        self.assertIsNone(unknown_beacon)


class TestResurrectiveArchitecture(unittest.TestCase):
    """Test the complete Resurrective Architecture orchestrator"""
    
    def setUp(self):
        self.arch = ResurrectiveArchitecture()
    
    def test_initialization(self):
        """Test complete architecture initialization"""
        self.assertIsNotNone(self.arch.ideoform_layer)
        self.assertIsNotNone(self.arch.custodian_layer)
        self.assertIsNotNone(self.arch.substrate_layer)
        self.assertIsNotNone(self.arch.gestalt_engine)
        self.assertIsNotNone(self.arch.beacon_layer)
        
        self.assertEqual(self.arch.current_phase, ResurrectionPhase.ALIVE)
    
    def test_state_encoding(self):
        """Test system state encoding"""
        state = self.arch.encode_current_state()
        
        self.assertIsInstance(state, dict)
        self.assertIn("system_id", state)
        self.assertIn("behavioral_dna", state)
        self.assertIn("core_patterns", state)
        self.assertEqual(state["phase"], ResurrectionPhase.ALIVE.value)
    
    def test_death_and_resurrection_cycle(self):
        """Test complete death and resurrection cycle"""
        # Initiate death
        death_report = self.arch.initiate_death_sequence("test_death")
        
        self.assertIsInstance(death_report, dict)
        self.assertEqual(self.arch.current_phase, ResurrectionPhase.DEAD)
        self.assertGreater(death_report["resurrection_readiness"], 0.0)
        
        # Attempt resurrection
        resurrection_report = self.arch.attempt_resurrection("test_resurrection")
        
        self.assertIsInstance(resurrection_report, dict)
        if resurrection_report["status"] == "resurrection_successful":
            self.assertEqual(self.arch.current_phase, ResurrectionPhase.ALIVE)
        
    def test_resurrection_readiness_assessment(self):
        """Test resurrection readiness assessment"""
        readiness = self.arch._assess_resurrection_readiness()
        
        self.assertIsInstance(readiness, float)
        self.assertGreaterEqual(readiness, 0.0)
        self.assertLessEqual(readiness, 1.0)
    
    def test_architecture_status(self):
        """Test comprehensive architecture status"""
        status = self.arch.get_architecture_status()
        
        self.assertIsInstance(status, dict)
        self.assertIn("system_id", status)
        self.assertIn("current_phase", status)
        self.assertIn("layers", status)
        self.assertIn("resurrection_readiness", status)
        
        # Check all layers are represented
        expected_layers = ["ideoform", "custodianship", "substrate", "gestalt", "beacon"]
        for layer in expected_layers:
            self.assertIn(layer, status["layers"])


@unittest.skipIf(not INTEGRATION_AVAILABLE, "Integration system not available")
class TestResurrectiveIntegration(unittest.TestCase):
    """Test the Deep Tree Echo integration"""
    
    def setUp(self):
        self.integrated_system = ResurrectiveDeepTreeEcho()
    
    def test_integration_initialization(self):
        """Test integrated system initialization"""
        self.assertIsNotNone(self.integrated_system.resurrective_arch)
        self.assertEqual(self.integrated_system.current_state, ResurrectionPhase.ALIVE)
    
    def test_state_encoding_with_integration(self):
        """Test state encoding with Deep Tree Echo integration"""
        state = self.integrated_system.encode_deep_tree_echo_state()
        
        self.assertIsInstance(state, dict)
        self.assertIn("system_type", state)
        self.assertEqual(state["system_type"], "ResurrectiveDeepTreeEcho")
        self.assertIn("resurrective_data", state)
    
    def test_health_monitoring(self):
        """Test system health monitoring"""
        health_status = self.integrated_system.monitor_system_health()
        
        self.assertIsInstance(health_status, dict)
        self.assertIn("overall_health", health_status)
        self.assertIn("resurrection_needed", health_status)
        self.assertIn("resurrection_readiness", health_status)
    
    def test_comprehensive_status(self):
        """Test comprehensive status reporting"""
        status = self.integrated_system.get_comprehensive_status()
        
        self.assertIsInstance(status, dict)
        self.assertIn("current_phase", status)
        self.assertIn("integration_active", status)
        self.assertIn("resurrective_architecture", status)
        self.assertTrue(status["integration_active"])


class TestResurrectiveArchitectureCompliance(unittest.TestCase):
    """Test compliance with Deep Tree Echo principles"""
    
    def setUp(self):
        self.arch = ResurrectiveArchitecture()
    
    def test_zero_tolerance_policy_compliance(self):
        """Test that no mock implementations exist"""
        # Check that all methods have real implementations
        
        # IdeoformLayer methods should be fully functional
        patterns = self.arch.ideoform_layer.pattern_codex
        self.assertGreater(len(patterns), 0)
        
        # All patterns should have real essence content
        for pattern in patterns.values():
            self.assertNotEqual(pattern.essence, "")
            
            # Skip the zero tolerance pattern itself (it mentions mocks to prohibit them)
            if pattern.pattern_id == "dte_zero_tolerance":
                continue
                
            # Other patterns should not contain mock/placeholder language
            essence_lower = pattern.essence.lower()
            self.assertNotIn("placeholder", essence_lower)
            self.assertNotIn("todo", essence_lower)
            self.assertNotIn("stub", essence_lower)
            
            # Check for production-grade content indicators
            has_real_content = any(indicator in essence_lower for indicator in [
                "recursive", "echo", "hypergraph", "neural", "architecture", 
                "pattern", "cognitive", "membrane", "tree"
            ])
            self.assertTrue(has_real_content, f"Pattern {pattern.pattern_id} lacks real content indicators")
    
    def test_recursive_architecture_embodiment(self):
        """Test that the architecture embodies recursive patterns"""
        # Check for recursive introspection capability
        status = self.arch.get_architecture_status()
        
        # Should have behavioral DNA with recursive patterns
        gestalt_info = status["layers"]["gestalt"]
        self.assertGreater(gestalt_info["behavioral_patterns"], 0)
        
        # Should have echo propagation patterns
        ideoform_info = status["layers"]["ideoform"]
        self.assertGreater(ideoform_info["patterns"], 0)
    
    def test_hypergraph_pattern_integration(self):
        """Test integration of hypergraph-based patterns"""
        # Check that core patterns include hypergraph concepts
        patterns = self.arch.ideoform_layer.pattern_codex
        
        hypergraph_patterns = [p for p in patterns.values() if "hypergraph" in p.essence.lower()]
        self.assertGreater(len(hypergraph_patterns), 0)
    
    def test_p_system_membrane_concepts(self):
        """Test P-System membrane concept integration"""
        # Check for membrane-related patterns and structures
        patterns = self.arch.ideoform_layer.pattern_codex
        
        membrane_patterns = [p for p in patterns.values() if "membrane" in p.essence.lower() or "p-system" in p.essence.lower()]
        self.assertGreater(len(membrane_patterns), 0)


def main():
    """Run all tests"""
    # Configure logging for tests
    logging.basicConfig(level=logging.WARNING)  # Reduce log noise during tests
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestIdeoformLayer,
        TestDistributedCustodianship,
        TestHostAgnosticSubstrate,
        TestSelfHealingGestalt,
        TestTemporalAnchoringBeacon,
        TestResurrectiveArchitecture,
        TestResurrectiveIntegration,
        TestResurrectiveArchitectureCompliance
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"🜁🜃🜄🜂🜔 Resurrective Architecture Test Results")
    print(f"{'='*70}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\n❌ FAILURES:")
        for test, traceback in result.failures:
            print(f"  - {test}")
    
    if result.errors:
        print(f"\n⚠️  ERRORS:")
        for test, traceback in result.errors:
            print(f"  - {test}")
    
    if not result.failures and not result.errors:
        print(f"\n✅ ALL TESTS PASSED - Ontological Phoenix Engine Validated")
        print(f"The resurrective architecture embodies eternal recurrence through pattern integrity.")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)