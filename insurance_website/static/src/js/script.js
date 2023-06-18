// odoo.define('insurance_website.form', function (require) {
//     'use strict';

//     const publicWidget = require('web.public.widget');

//     publicWidget.registry.InsuranceForm = publicWidget.Widget.extend({
//         selector: '.insurance-form',
//         events: {
//             'change #insurance_type': '_onInsuranceTypeChange',
//             'change .form-control': '_onFieldChange',
//         },

//         /**
//          * Handle change event for insurance type drop-down list
//          */
//         _onInsuranceTypeChange: function (ev) {
//             // Hide all fields for all types of insurance
//             this.$('.insurance-fields').hide();

//             // Show only the fields for the selected type of insurance
//             const selectedInsuranceType = this.$('#insurance_type').val();
//             if (selectedInsuranceType) {
//                 this.$(`#${selectedInsuranceType}_insurance_fields`).show();
//             }
//         },

//         /**
//          * Handle change event for form fields
//          */
//         _onFieldChange: function (ev) {
//             // Get the target field
//             const $field = $(ev.currentTarget);

//             // Change the color of the text part of the field
//             $field.css('color', 'red');
//         },
//     });
// });
// odoo.define('insurance_website.form', function (require) {
//     'use strict';

//     const publicWidget = require('web.public.widget');

//     publicWidget.registry.InsuranceForm = publicWidget.Widget.extend({
//         selector: '.insurance-form',
//         events: {
//             'change #insurance_type': '_onInsuranceTypeChange',
//             'change .form-control': '_onFieldChange',
//             'change #insurance_category_id': '_onInsuranceCategoryIdChange',
//             'change #insurance_sub_category_id': '_onInsuranceSubCategoryIdChange',
//         },

//         /**
//          * Handle change event for insurance type drop-down list
//          */
//         _onInsuranceTypeChange: function (ev) {
//             // Hide all fields for all types of insurance
//             this.$('.insurance-fields').hide();

//             // Show only the fields for the selected type of insurance
//             const selectedInsuranceType = this.$('#insurance_type').val();
//             if (selectedInsuranceType) {
//                 this.$(`#${selectedInsuranceType}_insurance_fields`).show();
//             }
//         },

//         /**
//          * Handle change event for form fields
//          */
//         _onFieldChange: function (ev) {
//             // Get the target field
//             const $field = $(ev.currentTarget);

//             // Change the color of the text part of the field
//             $field.css('color', 'red');
//         },

//         /**
//          * Handle change event for insurance category drop-down list
//          */
//         _onInsuranceCategoryIdChange: function (ev) {
//             // Get the selected category ID
//             const categoryId = parseInt(this.$('#insurance_category_id').val());

//             // Get the subcategory select element
//             const $subCategorySelect = this.$('#insurance_sub_category_id');

//             // Clear the current options
//             $subCategorySelect.empty();

//             // Add a default option
//             $subCategorySelect.append($('<option>', {
//                 value: '',
//                 text: '--Select Sub Category--'
//             }));

//             // Get the subcategories related to the selected category
//             this._getSubCategories(categoryId).then(subCategories => {
//                 // Populate the subcategory select element with new options
//                 for (const subCategory of subCategories) {
//                     $subCategorySelect.append($('<option>', {
//                         value: subCategory.id,
//                         text: subCategory.name
//                     }));
//                 }
//             });
//         },

//         /**
//          * Handle change event for insurance subcategory drop-down list
//          */
//         _onInsuranceSubCategoryIdChange: function (ev) {
//             // Get the selected subcategory ID
//             const subCategoryId = parseInt(this.$('#insurance_sub_category_id').val());

//             // Get the insurance policy select element
//             const $policySelect = this.$('#insurance_policy_id');

//             // Clear the current options
//             $policySelect.empty();

//             // Add a default option
//             $policySelect.append($('<option>', {
//                 value: '',
//                 text: '--Select Insurance Policy--'
//             }));

//             // Get the insurance policies related to the selected subcategory
//             this._getPolicies(subCategoryId).then(policies => {
//                 // Populate the insurance policy select element with new options
//                 for (const policy of policies) {
//                     $policySelect.append($('<option>', {
//                         value: policy.id,
//                         text: policy.policy_name
//                     }));
//                 }
//             });
//         },

//         /**
//          * Get subcategories related to the specified category ID
//          */
//         _getSubCategories: function (categoryId) {
//             return this._rpc({
//                 model: 'insurance.sub.category',
//                 method: 'search_read',
//                 domain: [['insurance_category_id', '=', categoryId]],
//                 fields: ['id', 'name']
//                 });        
//         },
//         _getPolicies: function (subCategoryId) {
//             return this._rpc({
//                 model: 'insurance.policy',
//                 method: 'search_read',
//                 domain: [['insurance_sub_category_id', '=', subCategoryId]],
//                 fields: ['id', 'policy_name']
//             });
//         },
//     });
// });
odoo.define('insurance_website.form', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.InsuranceForm = publicWidget.Widget.extend({
        selector: '.insurance-form',
        events: {
            'change #insurance_category_id': '_onInsuranceCategoryIdChange',
            'change #insurance_sub_category_id': '_onInsuranceSubCategoryIdChange',
            'change #insurance_policy_id': '_onInsurancePolicyIdChange',
        },

        /**
         * Handle change event for insurance category drop-down list
         */
        _onInsuranceCategoryIdChange: function (ev) {
            // Get the selected category ID
            const categoryId = parseInt(this.$('#insurance_category_id').val());

            // Get the subcategory select element
            const $subCategorySelect = this.$('#insurance_sub_category_id');

            // Hide all options except the first one
            $subCategorySelect.find('option:not(:first)').hide();

            // Show only the options related to the selected category
            $subCategorySelect.find(`option[data-category-id="${categoryId}"]`).show();

            // Reset the value of the subcategory select element
            $subCategorySelect.val('');

            // Trigger change event for subcategory select element
            $subCategorySelect.trigger('change');
        },

        /**
         * Handle change event for insurance subcategory drop-down list
         */
        _onInsuranceSubCategoryIdChange: function (ev) {
            // Get the selected subcategory ID
            const subCategoryId = parseInt(this.$('#insurance_sub_category_id').val());

            // Get the insurance policy select element
            const $policySelect = this.$('#insurance_policy_id');

            // Hide all options except the first one
            $policySelect.find('option:not(:first)').hide();

            // Show only the options related to the selected subcategory
            $policySelect.find(`option[data-subcategory-id="${subCategoryId}"]`).show();

            // Reset the value of the insurance policy select element
            $policySelect.val('');
        },
        /**
         * Handle change event for insurance policy drop-down list
         */
        _onInsurancePolicyIdChange: function (ev) {
            // Get the selected policy amount
            const policyAmount = parseFloat(this.$('#insurance_policy_id option:selected').data('policy-amount'));

            // Calculate the total policy amount
            const totalPolicyAmount = policyAmount * 12;

            // Calculate the monthly installment
            const monthlyInstallment = totalPolicyAmount / 12;

            // Update the hidden fields with the calculated values
            this.$('#policy_amount').val(policyAmount);
            this.$('input[name="total_policy_amount"]').val(totalPolicyAmount);
            this.$('input[name="duration"]').val(12);
            this.$('input[name="monthly_installment"]').val(monthlyInstallment);
        },
    });
});