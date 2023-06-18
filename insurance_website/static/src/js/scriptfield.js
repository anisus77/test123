odoo.define('insurance_website.form', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.InsuranceForm = publicWidget.Widget.extend({
        selector: '.insurance-form',
        events: {
            'change #insurance_category_id': '_onInsuranceCategoryIdChange',
            'change #insurance_sub_category_id': '_onInsuranceSubCategoryIdChange',
        },

        /**
         * Handle change event for insurance category drop-down list
         */
        _onInsuranceCategoryIdChange: function (ev) {
            // Get the selected category ID
            const categoryId = parseInt(this.$('#insurance_category_id').val());

            // Get the subcategory select element
            const $subCategorySelect = this.$('#insurance_sub_category_id');

            // Clear the current options
            $subCategorySelect.empty();

            // Add a default option
            $subCategorySelect.append($('<option>', {
                value: '',
                text: '--Select Sub Category--'
            }));

            // Get the subcategories related to the selected category
            this._getSubCategories(categoryId).then(subCategories => {
                // Populate the subcategory select element with new options
                for (const subCategory of subCategories) {
                    $subCategorySelect.append($('<option>', {
                        value: subCategory.id,
                        text: subCategory.name
                    }));
                }
            });
        },

        /**
         * Handle change event for insurance subcategory drop-down list
         */
        _onInsuranceSubCategoryIdChange: function (ev) {
            // Get the selected subcategory ID
            const subCategoryId = parseInt(this.$('#insurance_sub_category_id').val());

            // Get the insurance policy select element
            const $policySelect = this.$('#insurance_policy_id');

            // Clear the current options
            $policySelect.empty();

            // Add a default option
            $policySelect.append($('<option>', {
                value: '',
                text: '--Select Insurance Policy--'
            }));

            // Get the insurance policies related to the selected subcategory
            this._getPolicies(subCategoryId).then(policies => {
                // Populate the insurance policy select element with new options
                for (const policy of policies) {
                    $policySelect.append($('<option>', {
                        value: policy.id,
                        text: policy.name
                    }));
                }
            });
        },

        /**
         * Get subcategories related to the specified category ID
         */
        _getSubCategories: function (categoryId) {
            return this._rpc({
                model: 'insurance.sub.category',
                method: 'search_read',
                domain: [['insurance_category_id', '=', categoryId]],
                fields: ['id', 'name']
            });
        },

        /**
         * Get insurance policies related to the specified subcategory ID
         */
        _getPolicies: function (subCategoryId) {
            return this._rpc({
                model: 'insurance.policy',
                method: 'search_read',
                domain: [['insurance_sub_category_id', '=', subCategoryId]],
                fields: ['id', 'name']
            });
        },
    });
});